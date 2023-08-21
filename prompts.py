from langchain.prompts import PromptTemplate 

prompt_template_questions = """
あなたは学習資料に基づいて練習問題を作成する専門家です。
あなたの目標は、学生に試験の準備をさせることです。
これを行うには、以下のテキストについて質問します: 

---- -------- 
{text} 
------------

学生の試験準備となる質問を作成します。
重要な情報を失わないようにしてください。

QUESTIONS: 
"""
PROMPT_QUESTIONS = PromptTemplate(template=prompt_template_questions, input_variables=["text"])

refine_template_questions = ( """
あなたは学習資料に基づいて練習問題を作成する専門家です。
あなたの目標は、学生の試験準備を支援することです。
ある程度の練習問題を受け取りました: {existing_answer}。
オプションがあります。既存の質問を絞り込むか、新しい質問を追加します
(必要な場合のみ) 以下にさらに詳しいコンテキストを示します。 
------------ 
{text} 
------------

新しいコンテキストを使用して、元の質問を日本語でで修正します。
コンテキストが役に立たない場合は、元の質問を提供してください。
質問:
"""
 )

REFINE_PROMPT_QUESTIONS = PromptTemplate( 
    input_variables=["existing_answer" ,"text"],
    template=refine_template_questions,
)