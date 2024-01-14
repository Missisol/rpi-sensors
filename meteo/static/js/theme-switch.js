window.addEventListener('load', () => {
	const themeSwitchers = document.querySelectorAll('.theme-switch');

	const setColorMode = (mode) => {
		// Mode was given
		if (mode && mode !== 'auto') {
			// Update data-* attr on html
			document.documentElement.setAttribute('data-force-color-mode', mode);
			// Persist in local storage
			window.localStorage.setItem('color-mode', mode);
			// Make sure the checkbox is up-to-date
			document.querySelector(`.theme-switch[value=${mode}]`).checked = true;
		}
		
		// No mode given (e.g. reset)
		if (!mode || mode === 'auto') {
			// Remove data-* attr from html
			document.documentElement.removeAttribute('data-force-color-mode');
			// Remove entry from local storage
			window.localStorage.removeItem('color-mode');
			// Make sure the checkbox is up-to-date, matching the system preferences
			document.querySelector(`.theme-switch--auto`).checked = true;
		}
	}

	[...themeSwitchers].forEach((radio) => {
		radio.addEventListener('change', (event) => {
			setColorMode(event.target.value);
		})
	})
})
