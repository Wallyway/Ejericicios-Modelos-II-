

function sumColumn(table, index) {
  console.log(table.tBodies[0].rows[0].cells[2].innerText)
  return Array.from(table.tBodies[0].rows)
    .map(row => Number(row.cells[index].innerText))
    .reduce((accumulator, current) => accumulator + current);
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

function downloadInvoice() {
  const doc = new jsPDF();
  doc.setFontSize(18);
  doc.text("Invoice", 10, 20);
  doc.setFontSize(12);
  doc.text(`Date: {(new Date()).toLocaleString()}`, 10, 30)
  rows = document.querySelector("#billingTbl tbody").rows


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
  console.log("shit")
  let row = event.target.closest("tr");
  if (!row) return;
  quantityCell = row.cells[1];
  priceCell = row.cells[2];
  if (event.target.classList.contains("add-btn")) {
    priceCell.innerText = Number(priceCell.innerText) + Number(priceCell.innerText) / Number(quantityCell.innerText)
    addUp(quantityCell, 1);
  } else if (event.target.classList.contains("take-off-btn")) {
    priceCell.innerText = Number(priceCell.innerText) - Number(priceCell.innerText) / Number(quantityCell.innerText);
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

document.getElementById('searchForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = document.getElementById('searchName').value;
  const age = document.getElementById('searchAge').value;
  const gender = document.getElementById('searchGender').value;
  let searchParams = new URLSearchParams();
  if (name) searchParams.append('name', name);
  if (age) searchParams.append('age', age);
  if (gender) searchParams.append('gender', gender);

  try {
    const response = await fetch(`/api/search?${searchParams}`);
    if (!response.ok) throw new Error('Search failed');
    const data = await response.json();
    const resultsList = document.getElementById('resultsList');
    resultsList.innerHTML = '';
    if (data.results && data.results.length > 0) {
      data.results.forEach(person => {
        const row = document.createElement('tr');
        row.innerHTML = `
                        <td>${person.name}</td>
                        <td>${person.age}</td>
                        <td>${person.gender}</td>
                        <td>
                          <button type="button" class="cart-btn">
                            <i class="fa-solid fa-cart-shopping"></i>
                          </button>
                        </td>
                      `;
        resultsList.appendChild(row);
      });
    } else {
      resultsList.innerHTML = '<tr><td colspan="3">No results found</td></tr>';
    }
  } catch (error) {
    document.getElementById('status').innerHTML = 'Error: ' + error.message;
  }
});

document.getElementById('addProductForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  console.log("yes2")
  const productData = {
    name: document.getElementById('productName').value,
    price: parseInt(document.getElementById('productPrice').value),
    category: document.getElementById('productCategory').value
  };

  try {
    const response = await fetch('/api/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(productData)
    });

    if (!response.ok) throw new Error('Failed to add product');
    const result = await response.json();

    if (result.status === 'success') {
      document.getElementById('status').innerHTML = 'Product added successfully';
      document.getElementById('addProductForm').reset();
    } else {
      throw new Error(result.message || 'Failed to add product');
    }
  } catch (error) {
    document.getElementById('status').innerHTML = 'Error: ' + error.message;
  }
});

