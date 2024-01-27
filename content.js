chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.action === "highlightDarkPatterns") {
            const darkPatterns = request.detectedPatterns;
            darkPatterns.forEach(pattern => {
                const regex = new RegExp(pattern, 'gi');
                document.body.innerHTML = document.body.innerHTML.replace(regex, `<span class="dark-pattern">${pattern}</span>`);
            });

            sendResponse({ detectedPatterns: darkPatterns });
        }
    }
);
