chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: "highlightDarkPatterns" }, function (response) {
        document.getElementById("result").innerHTML = response.detectedPatterns.length > 0
            ? `Dark patterns detected: ${response.detectedPatterns.join(', ')}`
            : 'No dark patterns detected.';
    });
});
