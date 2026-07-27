console.log("script.js loaded");

document.addEventListener("DOMContentLoaded", function () {
    const urlInput = document.getElementById("website-url");
    const intervalSelect = document.getElementById("interval");

    const checkButton = document.getElementById("check-button");
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");

    const statusUrl = document.getElementById("status-url");
    const websiteStatus = document.getElementById("website-status");
    const statusCode = document.getElementById("status-code");
    const incidentNumber = document.getElementById("incident-number");
    const incidentAction = document.getElementById("incident-action");
    const monitoringState = document.getElementById("monitoring-state");

    function validateUrl() {
        const url = urlInput.value.trim();

        if (!url) {
            alert("Please enter a website URL");
            return null;
        }

        return url;
    }

    function updateStatusStyle(status) {
        websiteStatus.classList.remove(
            "status-up",
            "status-down",
            "status-unknown"
        );

        if (status === "UP") {
            websiteStatus.classList.add("status-up");
        } else if (status === "DOWN") {
            websiteStatus.classList.add("status-down");
        } else {
            websiteStatus.classList.add("status-unknown");
        }
    }

    function updateMonitoringStyle(isRunning) {
        monitoringState.classList.remove(
            "monitoring-running",
            "monitoring-stopped"
        );

        if (isRunning) {
            monitoringState.classList.add("monitoring-running");
        } else {
            monitoringState.classList.add("monitoring-stopped");
        }
    }

    async function checkWebsite() {
        const url = validateUrl();

        if (!url) {
            return;
        }

        checkButton.disabled = true;
        checkButton.textContent = "Checking...";

        try {
            const response = await fetch("/monitor/check", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    url: url
                })
            });

            const data = await response.json();

            if (!response.ok) {
                alert(data.detail || "Website check failed");
                return;
            }

            statusUrl.textContent = url;
            websiteStatus.textContent = data.status;
            statusCode.textContent = data.status_code ?? "No response";
            incidentNumber.textContent = data.incident_number ?? "None";
            incidentAction.textContent = data.incident_action ?? "None";

            updateStatusStyle(data.status);

        } catch (error) {
            console.error("Check error:", error);
            alert("Unable to connect to the backend");
        } finally {
            checkButton.disabled = false;
            checkButton.innerHTML = "<span>🔍</span> Check Website";
        }