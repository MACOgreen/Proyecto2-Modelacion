from matplotlib import pyplot as plt
import networkx as nx
from sympy import true


"""datas = [
    {
        "activity": "a",
        "duration": 2,
        "predecessors": ["start"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "b",
        "duration": 5,
        "predecessors": ["start"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "c",
        "duration": 4,
        "predecessors": ["a"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "d",
        "duration": 6,
        "predecessors": ["b", "c"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "e",
        "duration": 3,
        "predecessors": ["d"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "f",
        "duration": 8,
        "predecessors": ["e"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "g",
        "duration": 10,
        "predecessors": ["e"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "end",
        "duration": 0,
        "predecessors": ["f", "g"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
]"""

data_unordered = [
    {
        "activity": "g",
        "duration": 10,
        "predecessors": ["e"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "f",
        "duration": 8,
        "predecessors": ["e"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "b",
        "duration": 5,
        "predecessors": [],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "c",
        "duration": 4,
        "predecessors": ["a"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "d",
        "duration": 6,
        "predecessors": ["b", "c"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "a",
        "duration": 2,
        "predecessors": [],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "e",
        "duration": 3,
        "predecessors": ["d"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
]


def main():
    ordered_list = order_data(data_unordered)
    cpm = cpm_algorithm(ordered_list)
    create_graph(get_critical_path(cpm), ordered_list)
    create_graph_simple(ordered_list)


def check_existency(incomplete, complete):
    # print("{}\n{}".format(incomplete, complete))
    cont = 0
    for node in incomplete:
        for node2 in complete:
            if node == node2["activity"]:
                cont += 1
    if cont == incomplete.__len__():
        return true
    else:
        return False


def order_data(data_list):
    start_act = {
        "activity": "start",
        "duration": 0,
        "predecessors": [],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    }
    end_act = {
        "activity": "end",
        "duration": 0,
        "predecessors": ["f", "g"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    }
    ordered_list = []
    not_end_nodes = []
    ordered_list.append(start_act)
    while data_list:
        for index, act in enumerate(data_list):
            if act["predecessors"]:
                if check_existency(act["predecessors"], ordered_list):
                    not_end_nodes.append(act["activity"])
                    ordered_list.append(act)
                    data_list.pop(index)
                    for index, x in enumerate(not_end_nodes):
                        if x in act["predecessors"]:
                            not_end_nodes.pop(index)
            else:
                act["predecessors"].append("start")
                ordered_list.append(act)
                data_list.pop(index)
    # for node in ordered_list:
    #    print(node)
    # print(not_end_nodes)
    end_act["predecessors"] = not_end_nodes
    # print(end_act)
    ordered_list.append(end_act)
    return ordered_list


def cpm_algorithm(data):
    for node in data:
        # print("{}: ".format(node["activity"]))
        preds = node["predecessors"]
        if preds.__len__() > 0:
            ef_list = [act["ef"] for act in data if act["activity"] in preds]
            ef = max(ef_list)
            node["es"] = ef
            node["ef"] = node["es"] + node["duration"]
            # print("[{}, {}]".format(node["es"], node["ef"]))
    for index, node in enumerate(reversed(data)):
        # print("{}: ".format(node["activity"]))
        if index > 0:
            lf_list = [
                act["ls"] for act in data if node["activity"] in act["predecessors"]
            ]
            lf = min(lf_list)
            node["lf"] = lf
            node["ls"] = node["lf"] - node["duration"]
            """print(
                "[{}, {}] || [{}, {}]".format(
                    node["es"], node["ef"], node["ls"], node["lf"]
                )
            )"""
        else:
            node["lf"] = node["ls"] = node["ef"]
            """print(
                "[{}, {}] || [{}, {}]".format(
                    node["es"], node["ef"], node["ls"], node["lf"]
                )
            )"""
    return data


def get_critical_path(activities):
    critical_list = []
    for act in activities:
        if act["ef"] - act["lf"] == 0:
            critical_list.append(act["activity"])
    # print(critical_list)
    return critical_list


def create_graph(critical_list, data):
    graph = nx.Graph()
    for node in data:
        str = "{}|{}\n{}|{}".format(node["es"], node["ef"], node["ls"], node["lf"])
        str2 = "{}:\n{}|{}\n{}|{}".format(
            node["activity"], node["es"], node["ef"], node["ls"], node["lf"]
        )
        print(str2)
        if node["activity"] in critical_list:
            graph.add_node(
                node["activity"],
                color="g",
                es=node["es"],
                ef=node["ef"],
                ls=["ls"],
                lf=node["lf"],
                Name=str,
            )
        else:
            graph.add_node(
                node["activity"],
                color="cyan",
                es=node["es"],
                ef=node["ef"],
                ls=["ls"],
                lf=node["lf"],
                Name=str,
            )
        try:
            for pred in node["predecessors"]:
                if node["activity"] in critical_list and pred in critical_list:
                    graph.add_edge(node["activity"], pred, color="g", weight=4)
                else:
                    graph.add_edge(node["activity"], pred, color="black", weight=2)
        except:
            continue
    labels = dict()
    names = nx.get_node_attributes(graph, "Name")
    for node in graph.nodes:
        labels[node] = f"{names[node]}\n"
    colors = nx.get_edge_attributes(graph, "color").values()
    node_color = nx.get_node_attributes(graph, "color").values()
    weights = nx.get_edge_attributes(graph, "weight").values()
    plt.figure(figsize=(12, 8))
    plt.title("CPM Graph")
    pos = nx.spring_layout(graph, scale=3)
    nx.draw(
        graph,
        pos,
        font_size=10,
        with_labels=True,
        font_weight="bold",
        verticalalignment="center",
        edge_color=colors,
        node_size=900,
        node_color=node_color,
        width=list(weights),
    )
    x_values, y_values = zip(*pos.values())
    y_max = max(y_values)
    y_min = min(y_values)
    y_margin = (y_max - y_min) * 0.20
    plt.ylim(y_min - y_margin, y_max + y_margin)
    shift = [0, 0.45]
    shifted_pos = {node: node_pos + shift for node, node_pos in pos.items()}
    nx.draw_networkx_labels(
        graph, shifted_pos, labels=labels, horizontalalignment="center"
    )
    # turn off frame
    plt.axis("off")
    plt.show()


def create_graph_simple(data):
    graph = nx.Graph()
    for node in data:
        graph.add_node(
            node["activity"],
            color="gray",
            es=node["es"],
            ef=node["ef"],
            ls=["ls"],
            lf=node["lf"],
            Name=str,
        )
        try:
            for pred in node["predecessors"]:
                graph.add_edge(node["activity"], pred, color="black", weight=2)
        except:
            continue
    colors = nx.get_edge_attributes(graph, "color").values()
    node_color = nx.get_node_attributes(graph, "color").values()
    weights = nx.get_edge_attributes(graph, "weight").values()
    plt.figure(figsize=(12, 8))
    plt.title("CPM Graph")
    pos = nx.spring_layout(graph, scale=3)
    nx.draw(
        graph,
        pos,
        font_size=10,
        with_labels=True,
        font_weight="bold",
        verticalalignment="center",
        edge_color=colors,
        node_size=900,
        node_color=node_color,
        width=list(weights),
    )
    x_values, y_values = zip(*pos.values())
    y_max = max(y_values)
    y_min = min(y_values)
    y_margin = (y_max - y_min) * 0.20
    plt.ylim(y_min - y_margin, y_max + y_margin)
    # turn off frame
    plt.axis("off")
    plt.show()


#main()
