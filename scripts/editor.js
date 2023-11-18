var editor = editor = monaco.editor.create(document.getElementById('editor'), {
    language: 'python',
    theme: 'vs-light',
    automaticLayout: true,
    FontFace: 'JetBrains Mono',
    fontSize: 16,
});

function getCode() {
    return editor.getValue();
}