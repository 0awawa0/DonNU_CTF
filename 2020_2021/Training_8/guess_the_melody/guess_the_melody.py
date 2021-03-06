from lib.types import IStdin, IStdout


guess = [
    "This is an easy one. Highly popular band in 1970s, and highly popular song. In late 2018 the movie about this band was released. Can you believe there are just two notes?\n(4x4) D3/8 D3/8 D3/8 D3/16 D3/16 D3/8 A2/8 P/4\n",
    "Well this one has more notes. But it won't be harder to guess it. Hint: this band is one of Big Four of Thrash Metal.\n(4x4) E2/4 E3/8 G3/8 A2#/8 A2/4 E3/8\n",
    "Number three on the most popular album of this band. By the way, frontman of this band shot himself.\n(4x4) E2/8 E2/8 F2/8 F2#/4 A2/8 F2#/8 A2/8 F2#/8 F2#/8 F2/8 E2/8 B2/8 E2/8 E2/4 B2/8 E2/8 F2/8 F2#/4 A2/8 F2#/8 A2/8 F2#/8 F2#/8 F2/8 E2/8 E2/8 B2/8 E2/8 E2/4\n",
    "This song's artist is known as King of Pop. No more words are needed.\n(4x4) F2#/8 C2#/8 E2/8 F2#/8 E2/8 C2#/8 B2/8 C2#/8\n",
    "Fun fact: once the artist of this song bit the bat's head off. Yeah, you know him.\n(4x4) F2#/8 F2#/8 C3#/8 F2#/8 D3/8 F2#/8 C3#/8 F2#/8 B2/8 A2/8 G2#/8 A2/8 B2/8 A2/8 G2#/8 E2/8\n",
    "Cover of the album with this song has an amplitude modulation picture on it.\n(4x4) F2/8 G2/8 A2#/4 G2/(2+4) F2/8 G2/8 A2#/4 G3/4 D3#/4 D3/4 C3/(4+4) A2#/8 C3/8 D3/4 C3/(4+2) A2#/8 C3/8 D3/4 D3/4 G2/(4+2)\n",
    "The lead guitarist of this band wears the collest hat and the sunglasses.\n(4x4) D5/8 D6/8 A5/8 G5/8 G6/8 A5/8 F6#/8 A5/8 D5/8 D6/8 A5/8 G5/8 G6/8 A5/8 F6#/8 A5/8 E5/8 D6/8 A5/8 G5/8 G6/8 A5/8 F6#/8 A5/8 E5/8 D6/8 A5/8 G5/8 G6/8 A5/8 F6#/8 A5/8 G5/8 D6/8 A5/8 G5/8 G6/8 A5/8 F6#/8 A5/8 G5/8 D6/8 A5/8 G5/8 G6/8 A5/8 F6#/8 A5/8\n",
    "19 years old artist and already worldwide popular.\n(4x4) G1/4 P/8 G1/8 A1#/8 G1/8 P/8 G1/8 P/8 G1/8 P/8 G1/8 A1#/8 G1/8 F1/4 G1/4 P/8 G1/8 A1#/8 G1/8 P/8 G1/8 P/8 G1/8 P/8 G1/8 A1#/8 G1/8 F1/4 C2/4 P/8 C2/8 D2#/8 C2/8 P/8 C2/8 P/8 C2/8 P/8 C2/8 D2#/8 C2/8 G2/4 D2/4 P/8 D2/8 F2#/8 D2/8 P/8 D1/8 P/8 D1/8 P/8 D1/8 P/2\n",
    "I'm pretty sure every of you have sang this song. And sometimes you were the one who this song was sung for\n(3x4) B3/4 B3/8 C4#/4. B3/4. E4/4. D4#/2. B3/4 B3/8 C4#/4. B3/4. F4#/4. E4/2. B3/4 B3/8 B4/4. A4/4. E4/4 E4/8 D4#/4. C4#/4. A4/4 A4/8 G4#/4. E4/4. F4#/4. E4/2.\n",
    "This is not the song but you totally have heard it watching one of the greatest movie ever. By the way, books are better. Name the movie\n(3x4) P/4 P/4 B3/4 E4/4. G4/8 F4#/4 E4/2 B4/4 A4/2. F4#/2. E4/4. G4/8 F4#/4 D4/2 F4/4 B3/(2.+2.) B3/4 E4/4. G4/8 F4#/4 E4/2 B4/4 D5/2 G5#/4 C5/2 A4/4 C5/4. B4/8 A4#/4 F4#/2 G4/4 E4/(2.+2.)\n",
    "Nice job! You have guessed all ten melodies. Now there is a bonus track. I realy don't think you will guess it, so this one costs 20 points\n(4x4) D5/4 D5/8 D5/8 E5/4 G5/8 A5/(8+8) B5/8 P/2 E5/8 G5/8 A5/4 B5/8 A5/8 G5/8 E5/8 G5/8 A5/4 B5/8 A5/4 G5/8 P/4\n"
]

songs = [
    "Under Pressure",
    "Enter Sandman",
    "Come as you are",
    "Billie Jean",
    "Crazy Train",
    "Do I wanna know",
    "Sweet child o' mine",
    "Bad Guy",
    "Happy Birthday",
    "Harry Potter",
    "We didn't start the fire"
]

flags = [
    "./src/ctf_tasks/guess_the_melody/flag1.txt",
    "./src/ctf_tasks/guess_the_melody/flag2.txt",
    "./src/ctf_tasks/guess_the_melody/flag3.txt",
    "./src/ctf_tasks/guess_the_melody/flag4.txt",
    "./src/ctf_tasks/guess_the_melody/flag5.txt",
    "./src/ctf_tasks/guess_the_melody/flag6.txt",
    "./src/ctf_tasks/guess_the_melody/flag7.txt",
    "./src/ctf_tasks/guess_the_melody/flag8.txt",
    "./src/ctf_tasks/guess_the_melody/flag9.txt",
    "./src/ctf_tasks/guess_the_melody/flag10.txt",
    "./src/ctf_tasks/guess_the_melody/flag11.txt",
]


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("Hi, do you like music? I, myself, love it! But those note sheets are just too complicated. All those clefs and time signatures and there are so much lines! So I came up with another system. Let me explain.\n")
    stdout.write("1) All notes are represented by letters C, D, E, F, G, A and B. Letter 'P' is used for pauses\n")
    stdout.write("2) Next to the letter there is a number showing which octave it is (you will find octaves numbers here https://en.wikipedia.org/wiki/octave). Example: C5\n")
    stdout.write("3) Also note can be followed by # to raise it by a half tone. Example: A5#\n")
    stdout.write("4) After that there is a slash ('/') followed by a note's length (1 - is a whole note, 2 - 1/2 of the whole, 4 - 1/4 of the whole etc.). Example: D4#/2\n")
    stdout.write("5) Moreover, to increase note's length by a half dot ('.') is used. Like this: F3#/4.\n")
    stdout.write("6) Also note length might be expressed by a numbers sum within the parentheses like 'B2/(2+4)'. This means the note length is equals to two notes (B2/2 and B2/4) together. That's a tie in standard music theory.\n")
    stdout.write("7) And at the very beginning of the line there is a time signature. (3x4) is for 3 1/4 notes per bar (waltz time signature).\n")
    stdout.write("8) So here is an example of a whole line:\n")
    stdout.write("\t(4x4) C4/4 D4/4 E4/4 F4/4 G4/4 A4/4 B4/4\n")
    stdout.write("Pretty easy isn't it? Now I will send you 10 melodies written in such notation. Try to guess what melody it is. For every guessed melody you will get the flag for 2 points.\nThat makes 20 points for the whole task. Now let's go. BTW, answers are case insensetive\n")
    stdout.write("\n")

    for i in range(11):
        stdout.write(guess[i])
        stdout.write("Answer >> ")
        stdout.flush()
        answer = stdin.readline()
        if answer.lower().strip() == songs[i].lower().strip():
            stdout.write("That's right! Go for the next one. Here is your flag: " + open(flags[i]).read() + "\n")
            stdout.write("\n")
        else:
            print(f"Should be {songs[i]} but {answer.lower().strip()} received")
            stdout.write("Nope!\n")
            exit(0)
