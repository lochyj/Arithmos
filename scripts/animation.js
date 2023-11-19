// UUID, callback, arguments, delay
animation_stack = []
animation_old = []
timeout_ids = []

animating = false

function animate() {

    if (!animating)
        animating = true

    if (animation_stack.length == 0) {
        return
    }

    console.log("animate()")

    var next = animation_stack.shift()

    animation_old.push(next)

    delay = next[3]

    id = setTimeout(anim = () => run_animation(next[1], next[0], next[2]), delay)

    timeout_ids.push(id)

}

// The function that will run the animation after the delay has finished.
// <callback> must only take one argument.
function run_animation(callback, id, data) {
    for (var i = 0; i < animation_old.length; i++) {
        if (animation_old[i][0] == id) {
            animation_old.splice(i, 1);
            break;
        }
    }

    timeout_ids.pop()

    console.log("run_animation()")

    callback(data)

    if (animation_stack.length == 0) {
        animating = false;
        return;
    }

}

function pause_animation() {
    animations_to_cancel = timeout_ids.length;

    for (var i = 0; i < timeout_ids.length; i++) {
        clearTimeout(timeout_ids[i]);
    }

    timeout_ids = [];

    for (var i = 0; i < animations_to_cancel; i++) {
        animation_stack.unshift(animation_old.pop());
    }
}

function resume_animation() {
    animate();
}

function cancel_animation() {
    animation_stack = []
    animation_old = []
    timeout_ids = []

    animating = false
}

function traverse_edge(from, to, set_colour, delay) {

    if (delay == null) {
        delay = 0;
    }

    animation_stack.push([uuidv4(), traverse_edge_internal, [from, to, set_colour], delay]);

    animate();

}

function traverse_edge_internal(arguments) {
    from = arguments[0];
    to = arguments[1];
    set_colour = arguments[2];

    const links = Graph.graphData().links;

    console.log(links)

    var edge = null;

    for (var i = 0; i < links.length; i++) {
        if (links[i].source.id == from && links[i].target.id == to) {
            edge = links[i];
            break;
        }
    }

    if (edge == null) {
        console.log("Edge not found");
        return;
    }

    modifyEdge(from, to, edge.label, set_colour);

    Graph.emitParticle(edge);

}

function pause() {
    Graph.pauseAnimation();
}

function resume() {
    Graph.resumeAnimation();
}