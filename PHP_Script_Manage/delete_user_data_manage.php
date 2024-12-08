<?php
$servername = "localhost";  // 데이터베이스 서버
$username = "opsw4";        // 사용자 이름
$password = "opswteam4!";   // 비밀번호
$dbname = "opsw4";          // 데이터베이스 이름

// MySQL 연결
$conn = new mysqli($servername, $username, $password, $dbname);

// 연결 확인
if ($conn->connect_error) {
    die("연결 실패: " . $conn->connect_error);
}

$id = isset($_GET['id']) ? $_GET['id'] : null;

// 데이터 유효성 확인
if ($id) {
    // 데이터 삭제 위한 SQL 쿼리 작성
    $sql = "DELETE FROM user_data WHERE id = $id";
    
    // 쿼리 실행
    if ($conn->query($sql) === TRUE) {
        echo "레코드 삭제 완료. ";
    } else {
        echo "에러: " . $conn->error;
    }
} else {
    echo "유효하지 않은 입력 데이터";
}

// 연결 종료
$conn->close();
?>