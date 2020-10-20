from flask import *
from datetime import datetime
import os
from threading import Thread
import threadhandler
from read_mindwave_mobile import *
import flaskwebgui
app = Flask(__name__) 
ui = flaskwebgui.FlaskUI(app)
class datapackMW : 
    Delta = []
    Theta = []
    LowAlpha = []
    HighAlpha = []
    LowBeta = []
    HighBeta = []
    LowGamma = []
    MedGamma = []
    AttentionLevel = []
    PoorSignalLevel = []
    Unknowdatapoint = []
    MeditationLevel = []
class datapack :
    name = None
    age = None
    tel = None
    mode = None
    sex = None
    email = None
    app_token = None
    sex = ""
    age = ""
    score = 0
    currquestion = 0
questions = {
    1 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้เบื่อ ทำอะไร ๆ ก็ไม่เพลิดเพลิน"
    } , 
    
    2 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้ไม่สบายใจ ซึมเศร้า หรือท้อแท้"
    } ,
    
    3 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้หลับยาก หรือหลับ ๆ ตื่น ๆ หรือหลับมากไป"
    } ,
    
    4 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้เหนื่อยง่าย หรือไม่ค่อยมีแรง"
    } ,
    
    5 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้เบื่ออาหาร หรือกินมากเกินไป"
    } ,
    
    6 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้รู้สึกไม่ดีกับตัวเอง คิดว่าตัวเองล้มเหลว หรือเป็นคนทำให้ตัวเอง หรือครอบครัวผิดหวัง"
    } ,
    
    7 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้สมาธิไม่ดีเวลาทำอะไร เช่น ดูโทรทัศน์ ฟังวิทยุ หรือทำงานที่ต้องใช้ความตั้งใจ"
    } ,
    
    8 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้พูดหรือทำอะไรช้าจนคนอื่นมองเห็น หรือกระสับกระส่ายจนท่านอยู่ไม่นิ่งเหมือนเคย"
    } ,
    
    9 : {"choice" : 
    { 1 : "น้อยมาก ",
      2 : "น้อย    ",
      3 : "ปานกลาง",
      4 : "มาก    ",
      5 : "มากที่สุด "
    },
    "question" : "ช่วงนี้คิดทำร้ายตนเอง หรือคิดว่าถ้าตาย ๆ ไปเสียคงจะดี"
    }
}
@app.route("/")
def render_home() :
    return render_template("index.html")

@app.route("/info")
def render_measure() :
   return render_template("info.html")

@app.route("/service/api/get/data/users/data_user/all/unisub/json")
def render_api() :
    data = {"name" : datapack.name , "age" : datapack.age ,
            "tel" : datapack.tel , "mode" : datapack.mode
            ,"sex" : datapack.sex , "email" : datapack.email }
    return jsonify(data)

@app.route("/bterror")
def render_error() :
    return render_template("bthandler.html")

@app.route("/measure" , methods = ["POST"])
def measure_render() :
    thread = None
    thread = Thread(target=threadhandler.startallfunc)
    try :
      bt_init()
      if check() == True :
          thread.start()
      else :
          return redirect("/bterror")
    except :
      return redirect("/bterror")
    return render_template("measure.html")

@app.route("/headdata")
def return_datapoint() :
    Delta = None
    Theta = None
    LowAlpha = None
    HighAlpha = None
    LowBeta = None
    HighBeta = None
    LowGamma = None
    MedGamma = None
    AttentionLevel = None
    MeditationLevel = None
    data = {}
    try :
        Delta = threadhandler.data.Delta[-1]
        Theta = threadhandler.data.Theta[-1]
        LowAlpha = threadhandler.data.LowAlpha[-1]
        HighAlpha = threadhandler.data.HighAlpha[-1]
        LowBeta = threadhandler.data.LowBeta[-1]
        HighBeta = threadhandler.data.HighBeta[-1]
        LowGamma = threadhandler.data.LowGamma[-1]
        MedGamma = threadhandler.data.MedGamma[-1]
        AttentionLevel = threadhandler.data.AttentionLevel[-1]
        MeditationLevel = threadhandler.data.MeditationLevel[-1]
        data = {"Delta" : Delta , "Theta" : Theta , "LowAlpha" : LowAlpha
        , "HighAlpha" : HighAlpha , "LowBeta" : LowBeta , "HighBeta" : HighBeta,
        "LowGamma" : LowGamma , "MedGamma" : MedGamma , "AttentionLevel" : AttentionLevel,
        "MeditationLevel" : MeditationLevel
         }
    except :
        print("error")
        data = {}
        
    return jsonify(data)

@app.route("/validation" , methods = ["POST"])
def render_validate() :
  datapack.currquestion +=1
  datapack.score += int(request.form["choice"])
  return redirect("/quiz")

@app.route("/quiz")
def render_quiz() :
  if datapack.currquestion <= 9 :
    return render_template("quizpage.html" , question = questions , curr_ques = datapack.currquestion)
  else :
    
    print(datapack.score)
    return redirect("/info")

@app.route("/quizpage" , methods=["POST"])
def render_quizpage() :
  if datapack.currquestion == 0 :
    try :
        data = request.form.get("birthday")
        datapack.age = datetime.now().year - int(data.split("/")[-1])
        data = str(request.form.get("first_name")) + " " + str(request.form.get("last_name"))
        datapack.name = data
        data = str(request.form.get("male"))
        datapack.sex = str(request.form.get("gender"))
        datapack.email = str(request.form.get("email"))
        datapack.tel = str(request.form.get("phone"))
        datapack.mode = str(request.form.get("subject"))
    except :
        print("ALREADY LOG IN")
        print(datapack.name)
        print(datapack.age)
        print(datapack.tel)
        print(datapack.mode)
        print(datapack.sex)
        print(datapack.email)
    datapack.currquestion +=1
  return redirect("/quiz")



# ui.fullscreen = True
# ui.run()
app.run(debug = True)
