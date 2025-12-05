console.log("Server is running...");

const LEDOn = async (pin) => {
  console.log("LED is ON");
  let response = await fetch('/speed?value=0.9');
  let print  = await response.text();
  console.log("Request to turn LED ON sent", print);
}

const LEDOff = async (pin) => {
  console.log("LED is OFF");
  let response = await fetch('/speed?value=0');
  let print  = await response.text();
  console.log("Request to turn LED OFF sent", print);
}

const speedUp = async () => {
  console.log("Speed Up 0.05");
  let response = await fetch('/speedUp');
  let print  = await response.text();
  console.log("Request to speedup sent", print);
}

const speedDown = async () => {
  console.log("Speed Down 0.05");
  let response = await fetch('/speedDown');
  let print  = await response.text();
  console.log("Request to speed Down sent", print);
}
