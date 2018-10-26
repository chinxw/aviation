function changeTab($el, tabName = "") {
	if (tabName == "")
		tabName = $el.attr('id');
	$('div[name="nav_tabs"]').addClass("hidden");
	$('a.side_nav_option').removeClass("active");
	$('#nav_tab_'+tabName).removeClass("hidden");
	$el.addClass("active");
}

function showHideLoadingOverlay(show) {
	$('div.loading_overlay').css("display", (show ? "block":"none"));
}

function startupFunctions() {
	populateFormFields();

	//the following is a fix for the navigation bar, where if the bar is too long
	//for the content then it will adjust the height accordingly
	$("div.side_nav").css("min-height", $("div.side_nav_tabs").css("height"));

	$.contextMenu({
		selector: 'span.logged_in_user_context_menu',
		trigger: 'left',
		callback: function(key, options) {
			var m = "clicked: " + key;
			console.log(m);
			console.log(options);
		},
		items: {
			"settings": {name: "Settings"},
			//"sep1": "---------",
		}
	});

	showHideLoadingOverlay(false);
}

function populateFormFields() {
	// $("div.form").each(function() {
	//
	// });

	$('input.form.button').each(function() {
		$(this).addClass("ui-button");
		$(this).addClass("ui-widget");
		$(this).addClass("ui-corner-all");
		$(this).css("padding", "5px 20px");
		$(this).css("font-size", "14px;");
	});

	$('div.decimal').each(function() {
		$(this).change(function() {
			var $input = $(this).find("input:first");
			var regex = /^-?[0-9]+(\.[0-9]+)?$/;
			if (!regex.test($input.val())) {
				$input.css("background", "red");
				$input.css("color", "white");
				alert("You have entered in an invalid value. Please type in a decimal value.");
			} else {
				$input.css("background", "white");
				$input.css("color", "black");
			}
		});
	});

	$('input.email').change(function() {
		if ($(this).val() != "") {
			var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
			if (!regex.test($(this).val())) {
				$(this).css("background", "red");
				$(this).css("color", "white");
				alert("You have entered in an invalid value. Please type in a valid email address.");
			} else {
				$(this).css("background", "white");
				$(this).css("color", "black");
			}
		}
	});
}

function convertToCurrency(number) {
	return "$"+number.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,');
}

function validateEl($selector) {
	// console.log($selector.val());
	//try to find its label
	$label = $selector.parent().find("label:first");
	if ($selector.val() == "" || $selector.val() == null) {
		alert("The field \"" + ($label.length ? $label.text() : "") + "\" is required.");
		$selector.focus();
		return false;
	}
	return true;
}

function setCookie(cname, cvalue, exdays, path = "/") {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=" + path;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function deleteCookie(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
