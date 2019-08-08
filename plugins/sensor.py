"""
Sensor Path output plugin
"""

import optparse
import sys
import re

from pyang import plugin
from pyang import statements

def pyang_plugin_init():
    plugin.register_plugin(SensorPlugin())

class SensorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'path')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['path'] = self

    def emit(self, ctx, modules, fd):
        print("Displaying Paths: ")
        emit_tree(modules, fd, ctx)
    
# Function: emit_tree
# Args:
#   - modules:  each YANG module in a file
#   - fd:       open file <stdout>
#   - ctx:      Context object containing command line arguments
def emit_tree(modules, fd, ctx):
    for module in modules:
        chs = [ ch for ch in module.i_children #first item in module
               if ch.keyword in statements.data_definition_keywords #checks if ch type (keyword) is 'container', 'leaf', 'leaf-list', 'list', 'choice', 'anyxml', 'anydata', 'uses', 'augment'
               ]
        # returns <keyword> <child> ~ "container span-monitor-session"
               
        print_children(chs, module, fd, ' ', ctx, 2)


def print_children(i_children, module, fd, prefix, ctx, level=0):
    for ch in i_children:
        print_node(ch, module, fd, prefix, ctx, level)


# Function: print_node
# Args:
#   - s:        current node ~ 'container xyz' or 'leaf xyz'
#   - module:   main module
#   - fd:       open file <stdout>
#   - prefix:   prefix -> " "
#   - ctx:      Context object containing command line arguments
def print_node(s, module, fd, prefix, ctx, level=0):

    # Declare Variables
    pathstr = ""

    # sets pathstr = /ethernet-span-cfg:span-monitor-session
    if not ctx.opts.jstree_no_path:
        pathstr = statements.mk_path_str(s, False)
    
    # Generate new pathstr
    pathstr = module.i_modulename + pathstr

    # Only print pathstr if the node is a leaf
    if (s.keyword == 'leaf'):
        print(pathstr)
    
    #recursive step
    if hasattr(s, 'i_children'):
        level += 1
        if s.keyword in ['choice', 'case']:
            print_children(s.i_children, module, fd, prefix, ctx, level)
        else:
            print_children(s.i_children, module, fd, prefix, ctx, level)