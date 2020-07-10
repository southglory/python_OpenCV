import tensorflow.compat.v1 as tf

with tf.Session() as sess:  # 텐서플로우 세션 연결 수립(->시작)
    # 상수 생성
    a = tf.constant(120, name="a")
    b = tf.constant(130, name="b")
    c = tf.constant(140, name="c")

    # 변수 생성
    v = tf.Variable(0, name="v")

    calc_op = a + b + c  # 수식
    assign_op = tf.assign(v, calc_op)  # 계산 결과와 변수 연결
    sess.run(assign_op)  # 연산 실행(run())

    print(sess.run(v))  # v에 담긴 값을 로드해서 출력