# -*- coding:utf-8 -*-
import os.path, sys
reload(sys)

sys.setdefaultencoding('utf-8')
pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

from models import EmotionTable, db

b = {u'\uc54a\uc740\ub370': [u'\uc54a/paa+\uc740\ub370/ecs', u'\uc54a/paa+\uc740/etm+\ub370/nbn', u'\uc54a/pvg+\uc740\ub370/ecs', u'\uc54a/pvg+\uc740/etm+\ub370/nbn', u'\uc54a/px+\uc740\ub370/ecs', u'\uc54a/px+\uc740/etm+\ub370/nbn'], u'\uc2ac\ud504\ub2e4': [u'\uc2ac\ud504/paa+\ub2e4/ef'], u'\uc6b0\uc6b8\ud558\uc9c0': [u'\uc6b0\uc6b8/ncps+\ud558/xsms+\uc9c0/ecs', u'\uc6b0\uc6b8/ncps+\ud558/xsms+\uc9c0/ecx', u'\uc6b0\uc6b8/ncps+\ud558/xsms+\uc9c0/ef'], u'\ub098\ub294': [u'\ub098/ncn+\ub294/jxc', u'\ub098/npp+\ub294/jxc', u'\ub098/pvg+\ub294/etm', u'\ub098/px+\ub294/etm', u'\ub098/pvg+\uc544/ecs+\ub294/jxc', u'\ub098/pvg+\uc544/ef+\ub294/etm', u'\ub098/px+\uc544/ecs+\ub294/jxc', u'\ub098/px+\uc544/ef+\ub294/etm', u'\ub0a0/pvg+\ub294/etm'], u'\ud558\ub098\ub3c4': [u'\ud558\ub098/nnc+\ub3c4/jxc', u'\ud558\ub098/nnc+\ub3c4/nbu', u'\ud558/pvg+\uc5b4/ecs+\ub098/jxc+\ub3c4/jxc', u'\ud558/pvg+\uc5b4/ecx+\ub098/px+\uc544/ecs', u'\ud558/pvg+\uc5b4/ecx+\ub098/px+\uc544/ef', u'\ud558/pvg+\uc5b4/ecx+\ub098/px+\uc544/ecs+\ub3c4/jxc', u'\ud558/px+\uc5b4/ecs+\ub098/jxc+\ub3c4/jxc', u'\ud558/px+\uc5b4/ecx+\ub098/px+\uc544/ecs', u'\ud558/px+\uc5b4/ecx+\ub098/px+\uc544/ef', u'\ud558/px+\uc5b4/ecx+\ub098/px+\uc544/ecs+\ub3c4/jxc', u'\ud558/pvg+\ub098/ecs+\ub3c4/jxc', u'\ud558/px+\ub098/ecs+\ub3c4/jxc']}

class TestAnalyzer():
    def get_emotion_point(self):
        analyzed_table = b

        string_sequence = '나는 하나도 우울하지 않은데 슬프다'.split(' ')

        for key in analyzed_table.keys():
            for value in analyzed_table[key]:
                emotion = self.compare_with_emotiontable(value) 
                if emotion:
                    print emotion, string_sequence.index(key), key
                    break  # analyzed_table[key]의 첫번째  value만 탐색
        return True


    def add_emotion_data(self, emotion, value):
        emotiontable = EmotionTable(emotion, unicode(value))
        db.session.add(emotiontable)
        db.session.commit()

    def compare_with_emotiontable(self, word):
        emotion_table = EmotionTable.query.all()
        emotion = ''

        print word
        for emotion_object in emotion_table:
            if emotion_object.value in word:

                emotion = emotion_object.emotion
                break 
        if emotion:
            return emotion

        return False

    def compare_with_amptable(self, word):
        amp_point = 1
        return amp_point

    def compare_with_changetable(self, word):
        change_flag = False
        return change_flag

a= TestAnalyzer()
a.get_emotion_point()

