import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import cm


def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400,
                          background_color='black').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)


def generate_barchart(word_counts):
    words, counts = zip(*word_counts)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(words, counts, color=cm.viridis(range(len(words))))
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Words')
    plt.xticks(rotation=45)
    st.pyplot(fig)


df = pd.read_csv('data_data_berita_cleaned_preprocess.csv')

st.title('Dashboard Word Cloud dan Bar Chart')

categories = df['kategori'].unique()
selected_category = st.selectbox('Pilih Kategori', categories)


category_df = df[df['kategori'] == selected_category]


combined_text = ' '.join(category_df['isi'])


st.subheader(f'Word Cloud untuk Kategori: {selected_category}')
# Menampilkan head dari dataframe
st.write("Head of the DataFrame:")
st.write(df.head())

# Menampilkan tail dari dataframe
st.write("Tail of the DataFrame:")
st.write(df.tail())
generate_wordcloud(combined_text)


word_counts = Counter(combined_text.split())


common_words = word_counts.most_common(10)


st.subheader(f'Top 10 Words in Category: {selected_category}')
generate_barchart(common_words)
