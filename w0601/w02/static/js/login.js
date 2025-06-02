if ('{{msg}}'=='0'){
    alert("아이디가 존재하지 않습니다. 회원가입을 하세요.");
}else if ('{{msg}}'=='1'){
    alert("반갑습니다. 로그인이 되었습니다.");
    location.href='/';
}else if ('{{msg}}'=='2'){
    alert("로그아웃 되었습니다.");
    location.href='/';
}else if ('{{msg}}'=='-1'){
    alert("비밀번호가 틀립니다 다시 입력하세요.");
}
