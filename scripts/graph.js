const Graph = ForceGraph()(document.getElementById('output'))

Graph.autoPauseRedraw(false)

Graph.cooldownTime()

Graph.nodeLabel("label")

Graph.linkDirectionalParticleSpeed(0.04)

Graph.linkWidth(4)

out = document.getElementById("output")

outWidth = out.clientWidth
outHeight = out.clientHeight

Graph.width(outWidth)
Graph.height(outHeight)

function getGraph() {
    return Graph
}

function addNode(id, label, color) {
    Graph.graphData().nodes.push({id: id, label: label, color: color})
    Graph.graphData(Graph.graphData())
}

function addEdge(source, target, label, color) {
    Graph.graphData().links.push({source: source, target: target, label: label, color: color})
    Graph.graphData(Graph.graphData())
}

// Below doesn't work 100% correctly

function modifyNode(id, label, colour) {
    const nodes = Graph.graphData().nodes;

    var node = null;

    for (var i = 0; i < nodes.length; i++) {
        if (nodes[i].id == id) {
            node = i;
            break;
        }
    }

    if (node == null) {
        console.log("Node not found");
        return;
    }

    nodes[node].label = label;
    nodes[node].color = colour;

    Graph.graphData({nodes: nodes, links: Graph.graphData().links});

}

function modifyEdge(source, target, label, colour) {
    const links = Graph.graphData().links

    var edge = null

    for (var i = 0; i < links.length; i++) {
        if (links[i].source.id == source && links[i].target.id == target) {
            edge = i;
            break;
        }
    }

    if (edge == null) {
        console.log("Edge not found");
        return;
    }

    links[edge].label = label;
    links[edge].color = colour;

    Graph.graphData({nodes: Graph.graphData().nodes, links: links});
}

function removeNode(id) {
    Graph.graphData().nodes.splice(id, 1)
    console.log(Graph.graphData())
    Graph.graphData(Graph.graphData())
}

function removeEdge(source, target) {
    Graph.graphData().links.splice(source, 1)
    Graph.graphData(Graph.graphData())
}

// -

function setNodeLabel(id, label) {
    const nodes = Graph.graphData().nodes
    nodes.forEach(node => {
        if (node.id == id)
            node.label = label
    })

    Graph.graphData({nodes: nodes, links: Graph.graphData().links})
}

function resetGraph() {
    Graph.graphData({nodes: [], links: []})
}

function setDirectional(boolean) {
    if (boolean == true)
        Graph.linkDirectionalArrowLength(6)
    else
        Graph.linkDirectionalArrowLength(0)
}