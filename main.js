function planTrip() {
  const d = dest.value;
  const b = budget.value;
  const da = days.value;
  const p = pref.value;

  window.location.href = `/plan?dest=${d}&budget=${b}&days=${da}&pref=${p}`;
}
