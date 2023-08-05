// 현재 날짜를 가져오기 위해 Date 객체를 생성합니다.
const today = new Date();

// 서울의 시간대를 고려하여 UTC 시간을 조정합니다. (GMT+9:00)
const seoulOffset = 9 * 60; // 분 단위로 계산 (9시간을 분으로 환산)
today.setMinutes(today.getMinutes() + seoulOffset);

// 년, 월, 일을 가져옵니다.
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, "0"); // 월은 0부터 시작하므로 1을 더하고, 두 자리 숫자로 만듭니다.
const day = String(today.getDate()).padStart(2, "0"); // 일자를 두 자리 숫자로 만듭니다.

// "YYYY-MM-DD" 형식으로 날짜를 출력합니다.
const formattedDate = `${year}-${month}-${day}`;
console.log(formattedDate);
