// const deleteVegButton = document.querySelector('.deleteVegetable');

// deleteVegButton.onclick = (e) => {
//     e.preventDefault();
//     alert('are you sure you want to delete this vegetable?');
//     window.location.href = '/vegetable/delete/' + e.target.dataset.id;
// }

function deleteVegetable(id) {
    prompt('are you sure you want to delete this vegetable? ' + id);

    // window.location.href = '/vegetable/delete/' + id;
}

Swal.fire('Any fool can use a computer')

console.log(SweetAlertResult)
