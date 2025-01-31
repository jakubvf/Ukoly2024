//
// Created by Jakub Václav Flasar on 18.11.2024.
//

#ifndef UKOL_5_MASOZRAVEC_H
#define UKOL_5_MASOZRAVEC_H

#include "zvire.h"

class Prostredi;

class Masozravec : public Zvire
{
public:
    Masozravec(int x, int y, Prostredi *prostredi);

    void konzumuj(Organismus *other) override;
    void rozmnozovani() override;
    char getTyp() override;
};


#endif //UKOL_5_MASOZRAVEC_H
