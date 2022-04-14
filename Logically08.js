let a = [
    {nama : 'durian', jumlah : 10},
    {nama : 'apel', jumlah : 10},
    {nama : 'mangga', jumlah : 20},
    {nama : 'jeruk', jumlah : 30},
    {nama : 'pepaya', jumlah : 10}
]

let max = a[0].jumlah;
for (let i = 1; i < a.length; i++) {
    if (a[i] > max) {
        max = a[i].jumlah
        let b = a[i].jumlah
    }
}