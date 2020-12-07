"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some
food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents;
bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible
for these regulations considered how long they would take to enforce!

For example, consider the following rules:

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant
plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be
valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny
    gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny
    gold bag.
    So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you
get all of it.)
"""
import re

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.dag import ancestors


class Day7(object):
    def __init__(self, input_file_path):
        with open(input_file_path, "r") as f:
            nodes_edges_list = f.readlines()

        self.bags = nx.DiGraph()

        nodes, edges_lists = map(list, zip(*[line.split(" bags contain ") for line in nodes_edges_list]))
        # Split individual edge descriptions
        edges_lists = [edges_list.split(", ") for edges_list in edges_lists]
        # remove unnecessary info, like "bag(s)(.)"
        edges_lists = list(map(lambda l: [re.sub(" bag[s]?[.]?$", "", s) for s in l], edges_lists))
        edges_tuples = list(
            map(lambda l: [tuple(re.split("([0-9]+)", s)[1:]) for s in l if re.match("([0-9]+)", s)], edges_lists)
        )
        # build edge structure. The weight of the edge will be the number of bags of the kind "destination" the "origin"
        # can hold
        for idx, node in enumerate(nodes):
            node_edges = []
            for edge in edges_tuples[idx]:
                if len(edge) == 2:  # care for bags that do not contain other bags
                    weight, dest = edge
                    node_edges.append((node.strip(), dest.strip(), {"weight": int(weight)}))
            self.bags.add_edges_from(node_edges)

    def draw_bags_graph(self):
        pos = nx.spring_layout(self.bags, k=2, scale=3)
        nx.draw(self.bags, pos, with_labels=True)
        labels = nx.get_edge_attributes(self.bags, "weight")
        nx.draw_networkx_edge_labels(self.bags, pos, edge_labels=labels)
        plt.show()

    def part_1(self):
        return len(ancestors(self.bags, "shiny gold"))

    def _count_bags_per_node(self, node):
        if len(self.bags[node]) == 0:
            return 0
        else:
            n_bags = 0
            for inner_node, attributes in list(self.bags[node].items()):
                n_bags += attributes["weight"] + attributes["weight"] * self._count_bags_per_node(inner_node)
            return n_bags

    def part_2(self):
        n_bags = 0
        for node, attributes in list(self.bags["shiny gold"].items()):
            n_bags += attributes["weight"] + attributes["weight"] * self._count_bags_per_node(node)

        return n_bags
