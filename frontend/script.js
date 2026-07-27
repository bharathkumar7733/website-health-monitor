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
    }

    async function startMonitoring() {
        const url = validateUrl();

        if (!url) {
            return;
        }

        const interval = Number(intervalSelect.value);

        startButton.disabled = true;
        startButton.textContent = "Starting...";

        try {
            const response = await fetch("/monitor/start", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    url: url,
                    interval: interval
                })
            });

            const data = await response.json();

            if (!response.ok) {
                alert(data.detail || "Unable to start monitoring");
                return;
            }

            monitoringState.textContent = "Running";
            statusUrl.textContent = url;

            updateMonitoringStyle(true);

            await loadMonitoringStatus();

        } catch (error) {
            console.error("Start error:", error);
            alert("Unable to start monitoring");
        } finally {
            startButton.disabled = false;
            startButton.innerHTML =
                "<span>▶</span> Start Monitoring";
        }
    }

    async function stopMonitoring() {
        stopButton.disabled = true;
        stopButton.textContent = "Stopping...";

        try {
            const response = await fetch("/monitor/stop", {
                method: "POST"
            });

            const data = await response.json();

            if (!response.ok) {
                alert(data.detail || "Unable to stop monitoring");
                return;
            }

            monitoringState.textContent = "Stopped";

            updateMonitoringStyle(false);

        } catch (error) {
            console.error("Stop error:", error);
            alert("Unable to stop monitoring");
        } finally {
            stopButton.disabled = false;
            stopButton.innerHTML =
                "<span>■</span> Stop Monitoring";
        }
    }

    async function loadMonitoringStatus() {
        try {
            const response = await fetch("/monitor/status");

            if (!response.ok) {
                throw new Error("Unable to load monitoring status");
            }

            const data = await response.json();

            monitoringState.textContent =
                data.running ? "Running" : "Stopped";

            updateMonitoringStyle(data.running);

            if (data.url) {
                statusUrl.textContent = data.url;
            }

            if (data.last_result) {
                websiteStatus.textContent = data.last_result.status;

                statusCode.textContent =
                    data.last_result.status_code ?? "No response";

                updateStatusStyle(data.last_result.status);
            }

        } catch (error) {
            console.error("Status error:", error);
        }
    }

    checkButton.addEventListener("click", checkWebsite);
    startButton.addEventListener("click", startMonitoring);
    stopButton.addEventListener("click", stopMonitoring);

    loadMonitoringStatus();

    setInterval(loadMonitoringStatus, 5000);
});