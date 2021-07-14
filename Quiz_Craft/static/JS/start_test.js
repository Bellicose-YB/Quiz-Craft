const url = window.location.href;
const quizbody = document.querySelector('#quiz-body')

var total_que, hours, minutes, sec;
var correct = [];
var st_id;
$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response) {
        st_id = response.student_id;
        const que = response.question
        var ids = 1;
        que.forEach(ele => {
            correct.push([ele.Que_id, ele.Correct, ele.score])
            var options = [ele.Correct, ele.Other1, ele.Other2, ele.Other3]
            shuffle(options)
            quizbody.innerHTML += 
            '<div>' + 
                '<h1 style="color: #ffffff;">'+ ele.statement +'</h1>' + 
                '<div class="form-check">' +
                    '<input class="form-check-input" type="radio" name="que_'+ ids +'" id="radio_'+ ids +'_1" value="'+ options[0] +'_'+ ele.Que_id +'">' +
                    '<label class="form-check-label" for="radio_'+ ids +'_1" style="color: #ffffff;">'+ options[0] +'</label>' +
                '</div>' +
                '<div class="form-check">' +
                    '<input class="form-check-input" type="radio" name="que_'+ ids +'" id="radio_'+ ids +'_2" value="'+ options[1] +'_'+ ele.Que_id +'">' +
                    '<label class="form-check-label" for="radio_'+ ids +'_2" style="color: #ffffff;">'+ options[1] +'</label>' +
                '</div>' +
                '<div class="form-check">' +
                    '<input class="form-check-input" type="radio" name="que_'+ ids +'" id="radio_'+ ids +'_3" value="'+ options[2] +'_'+ ele.Que_id +'">' +
                    '<label class="form-check-label" for="radio_'+ ids +'_3" style="color: #ffffff;">'+ options[2] +'</label>' +
                '</div>' +
                '<div class="form-check">' +
                    '<input class="form-check-input" type="radio" name="que_'+ ids +'" id="radio_'+ ids +'_4" value="'+ options[3] +'_'+ ele.Que_id +'">' +
                    '<label class="form-check-label" for="radio_'+ ids +'_4" style="color: #ffffff;">'+ options[3] +'</label>' +
                '</div>' +
            '</div>';
            ids++;
        });
        quizbody.innerHTML += '<button type="submit" onclick="submitquiz()">Submit</button>';
        total_que = ids - 1;
    },
    error: function(err) {
        console.log(err)
    }
})

function shuffle(array) {
    var currentIndex = array.length,  randomIndex;
    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
    return array;
}

function submitquiz() {
    var total_score = 0;
    for(let i = 1;i <= total_que; i++) {
        for(let j = 1; j <= 4; j++) {
            var option = document.getElementById("radio_" + i + '_' + j);
            if(option.checked) {
                var arr = option.value.split('_');
                for(let k = 0; k < correct.length; k++) {
                    if(correct[k][0] == arr[1] && correct[k][1] == arr[0]) {
                        total_score += correct[k][2];
                    }
                }
            }
        }
    }
    var hashids = new Hashids();
    console.log(st_id)
    document.location.href = "http://127.0.0.1:8000/complete-test/" + st_id + "/" + hashids.encode(total_score);
}