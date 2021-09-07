# CS1010S Extra Practice Questions
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=RussellDash332/practice-makes-perfect)

Post-tutorial extra practice questions. Meant for educational purposes.

### Files
|PDF|tex|py|
|:---:|:---:|:--:|
|[Extra Practice 1](https://github.com/RussellDash332/practice-makes-perfect/blob/main/01/extra-1.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/01/extra-1.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/01/py)|
|[Extra Practice 2](https://github.com/RussellDash332/practice-makes-perfect/blob/main/02/extra-2.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/02/extra-2.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/02/py)|
|[Extra Practice 3](https://github.com/RussellDash332/practice-makes-perfect/blob/main/03/extra-3.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/03/extra-3.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/03/py)|
|[Extra Practice 4](https://github.com/RussellDash332/practice-makes-perfect/blob/main/04/extra-4.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/04/extra-4.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/04/py)|
|[Extra Practice 5](https://github.com/RussellDash332/practice-makes-perfect/blob/main/05/extra-5.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/05/extra-5.tex)|None|
|[Extra Practice 6](https://github.com/RussellDash332/practice-makes-perfect/blob/main/06/extra-6.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/06/extra-6.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/06/py)|
|[Extra Practice 7](https://github.com/RussellDash332/practice-makes-perfect/blob/main/07/extra-7.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/07/extra-7.tex)|None|
|[Extra Practice 8](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8.pdf) ([Abridged](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8q.pdf))|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8.tex)[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/08/extra-8q.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/08/py)|
|[Extra Practice 9](https://github.com/RussellDash332/practice-makes-perfect/blob/main/09/extra-9.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/09/extra-9.tex)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/tree/main/09/py)|
|[Mock Midterm](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Midterm/mock-midterm.pdf)|[✔️](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Midterm/mock-midterm.tex)|[Solutions](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Midterm/mock-midterm-solutions.py)|
|[Mock Finals](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Finals/mock-finals.pdf)|[
❌](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Finals/mock-finals.tex)|[Solutions](https://github.com/RussellDash332/practice-makes-perfect/blob/main/Mock/Finals/mock-finals-solutions.py)|

### Nerd Guide
- Clone this repository and make sure you have a local LaTeX compiler. You can get one by running the following on your command line (assuming Ubuntu 20.04.2 and TeXLive 2019)
    ```sh
    sudo apt -y install inkscape && export _INKSCAPE_GC=disable
    sudo apt -y install texlive-latex-base
    sudo apt -y install texlive-latex-recommended
    sudo apt -y install texlive-pictures
    sudo apt -y install texlive-latex-extra
    sudo apt -y install texlive-fonts-extra
    ```
- Go to the working directory of your tex files and run `make`. For example, to generate Extra Practice 1, run
    ```sh
    cd ~/practice-makes-perfect/01
    make
    ```
- For Extra Practice 8, I decided to create the abridged version, i.e. no Python sample execution. Instead of `make`, run `make q`.

### Credits
- [Eric Leow Yu Quan](https://github.com/shittake)
- [Sean Gee Zhing](https://github.com/pikasean)