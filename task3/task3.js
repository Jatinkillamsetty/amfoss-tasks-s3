const c = document.getElementById("jatin");
const d = c.getContext("2d");

let points = [];
const cx = 150;
const cy = 150;
let highestScore = 0;

d.beginPath();
d.arc(cx, cy, 3, 0, Math.PI * 2);
d.fill();

c.addEventListener("mousedown", startDraw);
c.addEventListener("mousemove", draw);
c.addEventListener("mouseup", endDraw);

function startDraw(e) {
    points = [];
    d.beginPath();
    d.moveTo(e.offsetX, e.offsetY);
    points.push([e.offsetX, e.offsetY]);
}

function draw(e) {
    if (e.buttons !== 1) return;
    d.lineTo(e.offsetX, e.offsetY);
    d.stroke();
    points.push([e.offsetX, e.offsetY]);
}

function endDraw() {
    let sumR = 0;
    let radii = [];

    points.forEach(([x, y]) => {
        let r = Math.hypot(x - cx, y - cy);
        radii.push(r);
        sumR += r;
    });

    let avgR = sumR / radii.length;

    let totalError = 0;
    radii.forEach(r => {
        totalError += Math.abs(r - avgR);
    });

    let avgError = totalError / radii.length;
    let accuracy = Math.max(0, 100 - (avgError / avgR) * 100);

    if (accuracy > highestScore) {
        highestScore = accuracy;
    }

    alert(`Accuracy: ${accuracy.toFixed(2)}%\nHighest Score: ${highestScore.toFixed(2)}%`);
    document.getElementById("accuracyDisplay").textContent = `${accuracy.toFixed(2)}%`;
    document.getElementById("highScoreDisplay").textContent = `${highestScore.toFixed(2)}%`

    d.clearRect(0, 0, c.width, c.height);

    d.beginPath();
    d.arc(cx, cy, 3, 0, Math.PI * 2);
    d.fill();
}
