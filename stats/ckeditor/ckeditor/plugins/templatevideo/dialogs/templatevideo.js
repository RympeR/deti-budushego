CKEDITOR.dialog.add( 'templatevideoDialog', function( editor ) {
    return {
        title: 'template video Properties',
        minWidth: 400,
        minHeight: 200,
        contents: [{
            id: 'tab-basic',
            label: 'Basic Settings',
            elements: [{
                    type: 'text',
                    id: 'videolink',
                    label: 'Video link',
                    validate: CKEDITOR.dialog.validate.notEmpty("video link field cannot be empty.")
                },
                {
                    type: 'text',
                    id: 'imagelink',
                    label: 'Image link',
                    validate: CKEDITOR.dialog.validate.notEmpty("image link field cannot be empty.")
                },
            ]
        }],


        onOk: function () {
            var dialog = this;
            editor.insertHtml(
                `<div class="video-area">
                <img src="${dialog.getValueOf( 'tab-basic', 'imagelink' )}" alt="class">
                <div class="${dialog.getValueOf( 'tab-basic', 'videolink' )}" class="video-button popup"><i class="flaticon-play"></i></div>
                </div>`
            );
        }
    }
});