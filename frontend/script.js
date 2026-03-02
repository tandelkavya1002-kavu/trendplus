const ctx = document.getElementById('sentimentChart');

new Chart(ctx,{
    type: 'pie',
    data:{
        labels: ['Positive','Negative','Neutral'],
        datasets:[{
            data:[45,30,35],
            backgroundColor: ['green','red','gray']
        }]
    }
}); 