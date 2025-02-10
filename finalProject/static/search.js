document.addEventListener('DOMContentLoaded', () => {    
  console.log("Hello")
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

