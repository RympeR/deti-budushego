CKEDITOR.dialog.add( 'templatevideoDialog', function( editor ) {
    return {
        title: 'template video Properties',
        minWidth: 400,
        minHeight: 200,
        contents: [{
            id: 'tab-basic',
            label: 'Настройки видео',
            elements: [
                {
                    type: 'text',
                    id: 'imagelink',
                    label: 'Ссылка на видео',
                    validate: CKEDITOR.dialog.validate.notEmpty("image link field cannot be empty.")
                },
            ]
        }],
        onOk: function () {
            var dialog = this;
            editor.insertHtml(
                `<iframe class="iframe-single-page video-area"  src="${dialog.getValueOf( 'tab-basic', 'imagelink' )}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`
            );
        }
    }
});