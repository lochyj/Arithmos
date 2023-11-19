function sanitizeHtml(html) {
    return html.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;").replace('\n', "<br>").replace('\"', "&quot;").replace('\'', "&apos;").replace(' ', "&nbsp;").replace('=', "&equals;")
}

function write(data, type) {
    const console = document.getElementById("console");

    data = sanitizeHtml(data)

    if (type == 0)
        console.innerHTML += "<span>" + data + "</span>";
    else if (type == 1)

        console.innerHTML += "<span style=\"color: lightcoral;\">" + data + "</span>";

}

function saveCode() {
    localStorage.setItem("arithmos_code", getCode());
}

function loadCode() {
    editor.setValue(localStorage.getItem("arithmos_code"));
}

function uuidv4() {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
}

