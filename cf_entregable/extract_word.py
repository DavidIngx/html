df['detected_words']=df['c_english'].apply(lambda x: emotion_count(x,vocab)[1])

words_used = []
words_used_df_powerbi = []


def extract_word_emotion(dictionary):
  words_used.append([dictionary["disgust"],
                      dictionary["joy"],
                      dictionary["anger"],
                      dictionary["sadness"],
                      dictionary["fear"],
                      dictionary["positive"],
                      dictionary["anticipation"],
                      dictionary["trust"],
                      dictionary["negative"],
                      dictionary["surprise"]])
  return True

def flat_list(row):
  if (len(row["words"]) == 0):
    pass
  else:
    for words_item in row["words"]:
      words_used_df_powerbi.append([row["emociones"], words_item])




# ejecutor 
df['detected_words'].apply(lambda dictionay: extract_word_emotion(dictionay))

word_used_df = pd.DataFrame(words_used, columns=["disgust",
                      "joy",
                      "anger",
                      "sadness",
                      "fear",
                      "positive",
                      "anticipation",
                      "trust",
                      "negative",
                      "surprise"])
step_1 = pd.melt(word_used_df, value_name="words", var_name="emociones")

# ejecutor 
step_1.apply(lambda row: flat_list(row) , axis=1)


word_cloud_emotion =pd.DataFrame(words_used_df_powerbi, columns=["emociones","word"])

word_cloud_emotion["segmento"] = "Salud"

english ={'anger':'enojo',
'boredom':'desinterés',
'empty':'vacio',
'fun':'diversión',
'happiness': 'felicidad',
'relief':'alivio',
'neutral':'neutral',
'worry':'preocupación',
'love':'amor',
'sadness':'incertidumbre',
'surprise':'sorpresa',
'hate':'odio',
'enthusiasm':'entusiasmo',
'joy':'disfrute',
'fear':'miedo',
'disgust':'disgusto',
'positive':'positivo',
'anticipation':'anticipación',
'trust':'confianza',
'negative':'negativo'
}
word_cloud_emotion["emociones"] = word_cloud_emotion["emociones"].apply(lambda emotion: english[emotion])
word_cloud_emotion.to_excel("data_final_salud.xlsx")
