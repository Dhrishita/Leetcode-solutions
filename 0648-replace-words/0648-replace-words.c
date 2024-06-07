bool startsWith(const char *word, const char *root) {
    while (*root) 
    {
        if (*root++ != *word++) 
        {
            return false;
        }
    }
    return true;
}
char* replaceWords(char** dictionary, int dictionarySize, char* sentence) {
    size_t sentenceLen = strlen(sentence);
    char* newSentence = (char*)malloc(sentenceLen + 1);
    if (!newSentence)
    {
        exit(EXIT_FAILURE);
    }
    newSentence[0] = '\0';

    
    char* sentenceCopy = strdup(sentence);
    if (!sentenceCopy) 
    {
        free(newSentence);
        exit(EXIT_FAILURE);
    }
    char* word = strtok(sentenceCopy, " ");
    while (word != NULL) 
    {
        char* replacement = word;
        for (int i = 0; i < dictionarySize; i++) 
        {
            if (startsWith(word, dictionary[i]) && strlen(dictionary[i]) < strlen(replacement)) 
            {
                replacement = dictionary[i];
            }
        }
        if (newSentence[0] != '\0') 
        {
            strcat(newSentence, " ");
        }
        strcat(newSentence, replacement);
        word = strtok(NULL, " ");
    }
    free(sentenceCopy);
    return newSentence;
}

