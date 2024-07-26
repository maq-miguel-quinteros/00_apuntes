# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default {
  // other rules...
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: ['./tsconfig.json', './tsconfig.node.json', './tsconfig.app.json'],
    tsconfigRootDir: __dirname,
  },
}
```

- Replace `plugin:@typescript-eslint/recommended` to `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`
- Optionally add `plugin:@typescript-eslint/stylistic-type-checked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and add `plugin:react/recommended` & `plugin:react/jsx-runtime` to the `extends` list

# Install

* Podemos utilizar pnpm para realizar las instalación y ejecutar/compilar el código. Consultar su uso en https://pnpm.io/es/installation

* React MUI: https://mui.com/material-ui/getting-started/installation/ podemos instalar la versión que viene que styled-component `npm install @mui/material @emotion/react @emotion/styled`. En el caso de MUI ya tienes los typos de typescript, es decir, no hace falta instalarlos. 

* instalamos styled component desde `npm install styled-components` https://styled-components.com/

* instalamos el complemento __React Create Component__ (opcional para probar) permite crear los componentes directamente, con su index que hace el export y definiendo el tipo para sus props

* utilizamos por buena practica barrel: __Auto Barrel for VSCode__ lo que hace es, en un archivo index.tsx exportar lo que contiene la carpeta donde se crea, por buenas prácticas creamos un barrel por cada carpeta. Tenemos la opción, con update barrel, de actualizar el listado cuando sumamos mas carpetas con componentes 

* podemos configurar un alias para el path src, para hacer más rapida la importación de componentes de la forma https://dev.to/avxkim/setup-path-aliases-w-react-vite-ts-poa




