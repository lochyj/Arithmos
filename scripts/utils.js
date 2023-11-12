function sanitizeHtml(html) {
    return html.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;").replace('\n', "<br>").replace('\"', "&quot;").replace('\'', "&apos;").replace(' ', "&nbsp;").replace('=', "&equals;")
}

function write(data, type) {
    const console = document.getElementById("console");

    if (type == 0)
        console.innerHTML += "<span>" + sanitizeHtml(data) + "</span>";
    else if (type == 1)
        console.innerHTML += "<span style=\"color: lightcoral;\">" + sanitizeHtml(data) + "</span>";

}