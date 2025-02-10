

function sumColumn(table, index) {
  console.log(table.tBodies[0].rows[0].cells[2].innerText)
  return Array.from(table.tBodies[0].rows)
    .map(row => Number(row.cells[index].innerText))
    .reduce((accumulator, current) => accumulator + current );
}

function addUp(element, number) {
  element.innerText = parseInt(element.innerText) + number;
}

function takeOff(element, number) {
  element.innerText = Math.max(0, parseInt(element.innerText) - number);
}

function addButton() {
  return `
  <button type="button" class="add-btn">
    <i class="fa-solid fa-plus"></i>
  </button>
  `;
}

document.getElementById("resultsTable").addEventListener("click", async (event) => {
  let row = event.target.closest("tr");
  if (!row) return;
  let cells = row.cells
  if (event.target.classList.contains("cart-btn")) {
    tBody = document.querySelector("#billingTbl tbody") 
    row = tBody.insertRow()
    console.log(cells[0].innerText)
    row.insertCell(0).textContent = cells[0].innerText
    row.insertCell(1).textContent = 1
    row.insertCell(2).textContent = cells[1].innerText
    row.insertCell(3).innerHTML = `
      <button type="button" class="add-btn">
      <i class="fa-solid fa-plus"></i>
      </button>
      `;
    row.insertCell(4).innerHTML = `
      <button type="button" class="take-off-btn">
        <i class="fa-solid fa-minus"></i>
      </button>
      `;
    row.insertCell(5).innerHTML = `
      <button type="button" class="remove-btn">
        <i class= "fa-solid fa-xmark"
      </button>
      `;
  }
});

document.getElementById("billingTbl").addEventListener("click", async (event) => {
  let row = event.target.closest("tr");
  if (!row) return;
  quantityCell = row.cells[1];
  if (event.target.classList.contains("add-btn")) {
    addUp(quantityCell, 1);
  } else if (event.target.classList.contains("take-off-btn")) {
    takeOff(quantityCell, 1); 
  } else if (event.target.classList.contains("remove-btn")) {
    row.remove()
  }
});

document.getElementById("billingBtn").addEventListener("click", async () => {
  table = document.getElementById("billingTbl", 1)
  footerRow = document.querySelector("#billingTbl tfoot tr")
  footerRow.cells[1].innerText = sumColumn(table, 1);
  footerRow.cells[2].innerText = sumColumn(table, 2);
});
