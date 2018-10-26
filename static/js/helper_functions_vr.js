function showHideEntity($element, show = true) {
	if (show) {
		if ($element.length) $element[0].setAttribute("visible", true);
		$element.find("*").each(function() {
			this.setAttribute("visible", true);
		});
	} else {
		if ($element.length) $element[0].setAttribute("visible", false);
		$element.find("*").each(function() {
			this.setAttribute("visible", false);
		});
	}
}

function videoNotLoadingFix() {
	//for some reason, videos do not start properly on mobile, this is a way to get around that problem
	$('video').each(function() {
		this.currentTime = 0;
		this.play();
		this.pause();
	});
}
