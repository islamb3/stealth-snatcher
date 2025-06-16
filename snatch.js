(async () => {
  const ipInfo = await fetch("https://api.ipify.org?format=json").then(res => res.json());
  const data = {
    ip: ipInfo.ip,
    ua: navigator.userAgent,
    platform: navigator.platform,
    lang: navigator.language,
    screen: `${screen.width}x${screen.height}`,
    tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
    date: new Date().toISOString()
  };

  fetch('snatch.php', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });
})();