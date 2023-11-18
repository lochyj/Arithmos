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