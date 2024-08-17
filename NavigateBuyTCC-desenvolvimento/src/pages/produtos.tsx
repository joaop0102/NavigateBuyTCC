import Navbar from "../components/navbar";
import Footer from "../components/footer";
import Card from "../components/card";
import React from "react";
import Head from "next/head";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/react";
import { ChevronDownIcon } from "@heroicons/react/20/solid";
import { AiOutlineArrowDown } from "react-icons/ai";
import "../app/globals.css";

const produtos: React.FC = () => {
  return (
    <main>
      <Head>
        <title>Navigate Buy</title>
      </Head>
      <Navbar />
      <div className="flex justify-center p-8">
        <h2 className="text-xl text-black">
          Produto pesquisado foi <span className="font-bold">“Fone”</span>
        </h2>
      </div>
      <div className="flex justify-center space-x-10 max-[400px]:ml-3">
        <h3 className="text-lg text-black">Mais de 50 resultados</h3>

        <Menu as="div" className="relative inline-block text-left">
          <div>
            <MenuButton className="inline-flex w-full justify-center gap-x-1 rounded-xl px-14 py-4 text-sm max-[400px]:text-xs bg-navigategreen text-white hover:bg-green-600">
              Filtrar por maior relevância
              <ChevronDownIcon aria-hidden="true" className="h-5 w-5 text-white" />
            </MenuButton>
          </div>

          <MenuItems transition className="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-xl bg-white border-2 border-navigategreen transition focus:outline-none data-[closed]:scale-95 data-[closed]:transform data-[closed]:opacity-0 data-[enter]:duration-100 data-[leave]:duration-75 data-[enter]:ease-out data-[leave]:ease-in">
            <MenuItem>
              <a href="#" className="block px-4 py-2 text-sm text-black data-[focus]:font-bold border-b border-navigategreen">
                Filtrar por maior relevância
              </a>
            </MenuItem>
            <MenuItem>
              <a href="#" className="block px-4 py-2 text-sm text-black data-[focus]:font-bold border-b border-navigategreen">
                Filtrar por menor preço
              </a>
            </MenuItem>
            <MenuItem>
              <a href="#" className="block px-4 py-2 text-sm text-black data-[focus]:font-bold border-b border-navigategreen">
                Filtrar por maior preço
              </a>
            </MenuItem>
            <MenuItem>
              <a href="#" className="block px-4 py-2 text-sm data-[focus]:font-bold text-black">
                Filtrar por melhor avaliação
              </a>
            </MenuItem>
          </MenuItems>
        </Menu>
      </div>
      <div className="grid grid-cols-4 max-[1050px]:grid-cols-2 max-[540px]:grid-cols-1">
        <Card
          imageSrc="./img/Fone MagaLu.png"
          heartIconSrc="./img/icon coração pintado.png"
          productDescription="Fone de Ouvido Esportivo Pulse PH333 - com Microfone Branco"
          brandName="Magazine Luiza"
          price="R$ 39,10" />
        <Card
          imageSrc="./img/Fone Mercado livre.png"
          heartIconSrc="./img/icon coração.png"
          productDescription="Fone de ouvido on-ear AKG K414 P preto"
          brandName="Mercado Livre"
          price="R$ 228,27" />
        <Card
          imageSrc="./img/Fone Casas Bahia.png"
          heartIconSrc="./img/icon coração.png"
          productDescription="Fones de Ouvido JBL Wave Buds Preto"
          brandName="Casas Bahia"
          price="R$ 236,55" />
        <Card
          imageSrc="./img/Fone Amazon.png"
          heartIconSrc="./img/icon coração.png"
          productDescription="JBL, Fone de Ouvido Sem Fio, Bluetooth, Wave Flex TWS - Preto"
          brandName="Amazon"
          price="R$ 331,19" />
      </div>
      <div className="grid grid-cols-4 max-[1050px]:grid-cols-2 max-[540px]:grid-cols-1">
        <Card
          imageSrc="./img/Fone Americanas.png"
          heartIconSrc="./img/icon coração.png"
          productDescription="Fone De Ouvido Bluetooth Sem Fio tws Compatível com Todos Celulares Microfone embutido"
          brandName="Americanas"
          price="R$ 30,71" />
        <Card
          imageSrc="./img/Fone Amazon 2.png"
          heartIconSrc="./img/icon coração.png"
          productDescription="Fone De Ouvido Sem Fio Bluetooth 5.3 Compatível iPhone Android Linha Premium AGOLD FN-BT10"
          brandName="Amazon"
          price="R$ 94,95" />
        <Card
          imageSrc="./img/Fone Mercado Livre 2.png"
          heartIconSrc="./img/icon coração pintado.png"
          productDescription="Fone de ouvido over-ear gamer Havit H2232D 2xP2, RGB - Preto"
          brandName="Mercado livre"
          price="R$ 103,55" />
        <Card
          imageSrc="./img/Fone Casas Bahia 2.png"
          heartIconSrc="./img/icon coração.png"
          productDescription="Fone de Ouvido Sem Fio Samsung Galaxy Buds FE - Branco"
          brandName="Mercado livre"
          price="R$ 381,65" />
      </div>
      <a href="#" className="flex justify-center text-xl">
        <p>Ver mais</p>
        <div className="p-[6px]">
          <AiOutlineArrowDown />
        </div>
      </a>
      <div className="p-16">
        <p className="text-center text-lg font-bold">Valores que custam os produtos</p>
        <div className="flex justify-center">
          <img src={"./img/tabela.png"} alt="" />
        </div>
      </div>
      <Footer />
    </main>
  );
};

export default produtos;
