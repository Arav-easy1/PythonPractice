try:
    print(3 / 2)
except Exception as e:
    print(e)
else:
    print("예외 없이 성공적으로 실행되었습니다.")
finally:
    print("예외 처리를 마칩니다.")