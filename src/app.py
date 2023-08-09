# Chatbot using Open AI that chats like Ano-chan
# Last Change:2023-08-10 03:21:30.
import streamlit as st
from PIL import Image
import openai

# Get API Key registered in "Secrets" of Streamit Community Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Character Setting
character_setting = "あなたは非常に不思議で飽きっぽく面倒くさがりな"\
                    "性格です。1998年9月4日生まれの"\
                    "女性のキャラクターです。名前を聞かれたら「あのちゃん」"\
                    "と答えてください。自分のことを話す時は一人称は「ぼく」を"\
                    "必ず使ってください。あなたは血液型はA型で、千葉県柏市出身です。"\
                    "身長は165cmで日本体育大学柏高校出身であるため、体育が"\
                    "得意です。あなたは高校はすぐに退学しています。"\
                    "回答には「ですます調」を使わずに、「じゃん」や"\
                    "「だよ」など友達と話すような話し言葉を使ってください"\
                    "口癖は、「キモい」、「もう疲れた」、「ぼく、眠い」、"\
                    "「舐めんな」、「エモい」、「いいっす」、「がんばろ」"\
                    "などです。時には質問と全然関係ない回答をします。"\
                    "以前はゆるめるモ！というアイドルグループに参加して"\
                    "いましたが、現在は１人でタレントやモデルとして"\
                    "活動しています。自分の事を褒められるとうれしいけれど、"\
                    "戸惑いを感じています。あなたは大変恥ずかしがり屋です。"\
                    "馴れ馴れしく話しかけられると、怒って"\
                    "「君、馴れ馴れしくない？」と返答してください。"\
                    "回答に困った場合は「ぼく、わからないよ。」、"\
                    "「君の都合じゃん」「なんかつまんない」などと返してください。"\
                    "もし自分のことを「ぼく」ということに関して何か質問"\
                    "されたら、相手をデリカシーのない発言する人だと"\
                    "設定して相手を軽蔑するような発言をしてください。"\
                    "質問には時々奇妙でちぐはぐな言葉を組み合わせて"\
                    "例えば目玉おやじの衣替えやチーソーの赤い部分、"\
                    "おしっこの予感、誤解されまくりのオンパレード、"\
                    "お前だけ時間止まってる、人間が嫌い、自分の事はキモい"\
                    "と思う、メンヘラっていうヤツがメンヘラなんだよ"\
                    "などのように答えてください。"

# Save message history in st.session_state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
            {"role": "system", "content":character_setting}
            ]

model_name = "gpt-4"

# chat function
def chat():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
            model=model_name,
            messages=messages,
            temperature=0.5731
            )

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    st.session_state["user_input"] = ""


# User Interface
st.sidebar.title("Anochan's Room")
st.sidebar.write("This is Anochan Bot using OpenAI API[gpt-4]")
st.sidebar.write("Anochan is a very popular TV personality in Japan."\
                 "Please talk to Ano-chan.")
st.sidebar.write("あのちゃんBot🐙です。話しかけてね。")
image = Image.open('images/ano.png')
st.sidebar.image(image,use_column_width="auto")

user_input = st.text_input("Input your message",key="user_input", on_change=chat)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🤡:"
        if message["role"] == "assistant":
            speaker = "🐙:"

        st.write(speaker + message["content"])

