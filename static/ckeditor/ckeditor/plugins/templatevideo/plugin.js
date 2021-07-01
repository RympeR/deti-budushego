CKEDITOR.plugins.add( 'templatevideo', {
    icons: 'templatevideo',
    init: function( editor ) {
        editor.addCommand( 'templatevideo', new CKEDITOR.dialogCommand( 'templatevideoDialog' ) );
        editor.ui.addButton( 'Templatevideo', {
            label: 'Insert template video block',
            command: 'templatevideo',
            toolbar: 'insert'
        });

        CKEDITOR.dialog.add( 'templatevideoDialog', this.path + 'dialogs/templatevideo.js' );
    }
});
