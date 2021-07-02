CKEDITOR.plugins.add( 'templatequote', {

	// Register the icons. They must match command names.
	icons: 'templatequote',

	// The plugin initialization logic goes inside this method.
	init: function( editor ) {

		// Define the editor command that inserts a timestamp.
		editor.addCommand( 'insertTemplatequote', {

			// Define the function that will be fired when the command is executed.
			exec: function( editor ) {
				var now = new Date();

				// Insert the timestamp into the document.
				editor.insertHtml( '<blockquote class="single-quote"><div class="quotes">[text]<span>[Author]</span></div></blockquote>' );
			}
		});

		// Create the toolbar button that executes the above command.
		editor.ui.addButton( 'Templatequote', {
			label: 'Insert Templatequote',
			command: 'insertTemplatequote',
			toolbar: 'insert'
		});
	}
});