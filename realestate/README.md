# Welcome to [Slidev](https://github.com/slidevjs/slidev)!

To start the slide show:

- `pnpm install` or with `npm install`
- `pnpm dev` or `npm run dev`
- visit <http://localhost:3030>

Edit the [slides.md](./slides.md) to see the changes.

Learn more about Slidev at the [documentation](https://sli.dev/).

---

```sh
cd ./realestate
#npm install -g @slidev/cli #install slidev globally
npm init slidev #yarn create slidev

#slidev #to restart it
```

```sh
npm install @iconify-json/uim #https://icon-sets.iconify.design/uim/?icon-filter=rocket&keyword=uim
npm install @iconify-json/logos
```

Or create via GHA CI/CD as done with the multichat [here](https://github.com/JAlcocerT/Streamlit-MultiChat/blob/main/.github/workflows/SliDev_CICD.yml#L39C1-L48C30).

```sh
#npm install
#npm run build #this is mapped to: slidev build, but wont accept the subroute for github pages
#slidev build
slidev build --base /Data-Chat/ 
```