import type { Metadata } from "next";
import "./globals.css";

import Editar from "../pages/editar-perfil"
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import Home from "../pages/home";
import Cadastro from "@/pages/cadastro";
import Login from "@/pages/login";
import Categorias from "@/pages/categorias";

export const metadata: Metadata = {
  title: "Login",
  description: "Faça o seu cadastro.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
      <>
      <Editar />
      </>
  );
}
