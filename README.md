# CS1010S Extra Practice Questions
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=RussellDash332/practice-makes-perfect)

> This repository has been combined with Keng Hwee's practice repository at [this repository](https://github.com/cs1010s/practice-makes-perfect). You can take a look there!

Post-tutorial extra practice questions. Meant for educational purposes on TA-ing [CS1010S: Programming Methodology](https://nusmods.com/modules/CS1010S/programming-methodology).

### Files
|Practice PDF|Solutions PDF|Python Files|
|:---:|:---:|:--:|
|[Extra Practice 1](https://github.com/RussellDash332/practice-makes-perfect/blob/main/01/extra-1.pdf)|[Solutions 1](https://github.com/RussellDash332/practice-makes-perfect/blob/main/01/extra-1-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/01/py)|
|[Extra Practice 2](https://github.com/RussellDash332/practice-makes-perfect/blob/main/02/extra-2.pdf)|[Solutions 2](https://github.com/RussellDash332/practice-makes-perfect/blob/main/02/extra-2-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/02/py)|
|[Extra Practice 3](https://github.com/RussellDash332/practice-makes-perfect/blob/main/03/extra-3.pdf)|[Solutions 3](https://github.com/RussellDash332/practice-makes-perfect/blob/main/03/extra-3-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/03/py)|
|[Extra Practice 4](https://github.com/RussellDash332/practice-makes-perfect/blob/main/04/extra-4.pdf)|[Solutions 4](https://github.com/RussellDash332/practice-makes-perfect/blob/main/04/extra-4-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/04/py)|
|[Extra Practice 5](https://github.com/RussellDash332/practice-makes-perfect/blob/main/05/extra-5.pdf)|[Solutions 5](https://github.com/RussellDash332/practice-makes-perfect/blob/main/05/extra-5-solutions.pdf)|-|
|[Extra Practice 6](https://github.com/RussellDash332/practice-makes-perfect/blob/main/06/extra-6.pdf)|[Solutions 6](https://github.com/RussellDash332/practice-makes-perfect/blob/main/06/extra-6-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/06/py)|
|[Extra Practice 7](https://github.com/RussellDash332/practice-makes-perfect/blob/main/07/extra-7.pdf)|[Solutions 7](https://github.com/RussellDash332/practice-makes-perfect/blob/main/07/extra-7-solutions.pdf)|-|
|[Extra Practice 8](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8.pdf)<br>([Abridged Version](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8q.pdf))|[Solutions 8](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/08/py)|
|[Extra Practice 9](https://github.com/RussellDash332/practice-makes-perfect/blob/main/09/extra-9.pdf)|[Solutions 9](https://github.com/RussellDash332/practice-makes-perfect/blob/main/09/extra-9-solutions.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/09/py)|
|[Mock Midterm](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Midterm/mock-midterm-unnerfed.pdf)<br>([Nerfed Version](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Midterm/mock-midterm.pdf))|-|[Solutions](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Midterm/mock-midterm-solutions.py)|
|[Mock Finals](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Finals/mock-finals.pdf)|-|[Solutions](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Finals/mock-finals-solutions.py)|

### Contribution Setup
- Clone this repository and make sure you have a local LaTeX compiler. You can get one by running the following on your command line (assuming Ubuntu 20.04.2 and TeXLive 2019)
    ```sh
    sudo apt -y install inkscape && export _INKSCAPE_GC=disable
    sudo apt -y install texlive-latex-base
    sudo apt -y install texlive-latex-recommended
    sudo apt -y install texlive-pictures
    sudo apt -y install texlive-latex-extra
    sudo apt -y install texlive-fonts-extra
    ```
- We will be using Makefile to render the TeX files into PDF files. For example, to render the question and solutions to Extra Practice 1 do the following.
    ```sh
    cd ~/practice-makes-perfect/01
    make    # Generates question
    make s  # Generates solutions
    ```
- For simplicity, you can just render everything by running `automate.sh`.
    ```sh
    cd ~/practice-makes-perfect
    ./automate.sh
    ```

### Credits
- [Eric Leow Yu Quan](https://github.com/shittake)
- [Sean Gee Zhing](https://github.com/pikasean)
- [Ng Keng Hwee](https://github.com/kenghweeng)
