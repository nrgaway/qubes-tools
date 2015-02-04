
(function ($) {
    var members = [
        "class",
        "exception",
        "classmethod",
        "method",
        "function",
        "module",
        "attribute",
        "data",
    ]

    /**
    * Add callout classes to section members
    */

    addCallout = function () {
        var outer = localStorage.getItem('toggle-callout-outer') || true;
        var inner = localStorage.getItem('toggle-callout-inner') || false;

        // outer
        if (String(outer).toLowerCase() === 'true') {
            for (var member in members) {
                $('.section > dl.' + members[member])
	            .addClass('callout')
            }
            $('#toggle-callout-outer').checkbox('check');
        }

        // inner
        if (String(inner).toLowerCase() === 'true') {
            for (var member_outer in members) {
                for (var member_inner in members) {
                    $('dl.' + members[member_outer]).find('dl.' + members[member_inner])
    	                .addClass('callout')
                }
                $('#toggle-callout-inner').checkbox('check');
            }
        }
    };

    getTitle = function(self) {
        console.log('self: ' + self.toString() );
        if ($(self).checkbox('is checked') ) {
          console.log('data-on-title: ' + $(self).attr('data-on-title'));
          return $(self).attr('data-on-title');
        } else {
          console.log('data-off-title: ' + $(self).attr('data-off-title'));
          return $(self).attr('data-off-title');
        }
    };

    getContent = function(self) {
        if ($(self).checkbox('is checked') ) {
          console.log('data-on-content: ' + $(self).attr('data-on-content'));
          return $(self).attr('data-on-content');
        } else {
          console.log('data-off-content: ' + $(self).attr('data-off-content'));
          return $(self).attr('data-off-content');
        }
    };

    $(document).ready(function () {
        // Enable button toggle
        $('.ui.checkbox').checkbox();

        // XXX: Move to semantic.js
        //$('.button').popup({
        //    inline: true,
        //    hide: true,
        //});

        // XXX: Move to semantic.js
        //$('.button').popup({
        //  on: 'hover',
        //      });

        // XXX: Move to semantic.js
        //$('.checkbox').popup({
        //  on: 'hover',
        //      });

        // XXX: Combine into one to allow all to use
        /*
        $('#toggle-callout-outer').popup({
          //on: 'hover',
          //debug: true,
          //verbose: true,
          title: getTitle($('#toggle-callout-outer')), 
          content: getContent($('#toggle-callout-outer')),
          position : 'bottom left',
          target: '#callout1'
        });
        */
        $('#toggle-callout-inner').popup({
          title: getTitle($('#toggle-callout-inner')), 
          content: getContent($('#toggle-callout-inner')),
          position : 'bottom left',
          target: '#callout2'
        });

        // Outer callout border toggle
        $('#toggle-callout-outer').on ({
            /*
            change: function(event) {
                $(this).popup('hide');
                $(this).popup({
                    title: getTitle(this),
                    content: getContent(this),
                    position : 'bottom left',
                });
            },
            */
            click: function(event) {
                for (var member in members) {
                    $('.section > dl.' + members[member])
	                    .toggleClass('callout');
                }
                // Store value on the browser beyond the duration of the session
                localStorage.setItem('toggle-callout-outer', $('#toggle-callout-outer').checkbox('is checked'));
            }
        });

        // Inner callout border toggle
        $('#toggle-callout-inner').on ({
            change: function(event) {
                $(this).popup('hide');
                $(this).popup({
                    title: getTitle(this),
                    content: getContent(this),
                    position : 'bottom left',
                });
            },
            click: function(event) {
                for (var member_outer in members) {
                    for (var member_inner in members) {
                        $('dl.' + members[member_outer]).find('dl.' + members[member_inner])
	                        .toggleClass('callout');
                    }
                }
                // Store value on the browser beyond the duration of the session
                localStorage.setItem('toggle-callout-inner', $('#toggle-callout-inner').checkbox('is checked'));
            }
        });

        // Enable mobile menu sidebar
        $('#menu_mobile').on ({
            click: function(event) {
                $('#menu_sidebar').sidebar('toggle');
            },
        });

        // Add callout classes
        addCallout();
    });
}(window.$jqTheme || window.jQuery));

// vim: ts=4 sw=4 et
