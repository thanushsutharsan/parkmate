/*jslint browser*/

// loads parking images from wikimedia commons
document.addEventListener("DOMContentLoaded", function () {
    const fallback = document.body.dataset.parkingFallback || "";
    const images = document.querySelectorAll("[data-parking-image]");
    const commonsEndpoint = "https://commons.wikimedia.org/w/api.php";

    async function searchCommons(searchText) {
        const params = new URLSearchParams({
            action: "query",
            format: "json",
            generator: "search",
            gsrlimit: "10",
            gsrnamespace: "6",
            gsrsearch: searchText,
            iiprop: "url",
            iiurlwidth: "900",
            origin: "*",
            prop: "imageinfo"
        });

        try {
            const response = await fetch(`${commonsEndpoint}?${params}`);

            if (!response.ok) {
                return null;
            }

            const data = await response.json();

            if (!data.query || !data.query.pages) {
                return null;
            }

            const pages = Object.values(data.query.pages);

            for (const page of pages) {
                const info = page.imageinfo && page.imageinfo[0];

                if (info) {
                    const imageUrl = info.thumburl || info.url;

                    if (imageUrl) {
                        return imageUrl;
                    }
                }
            }
        } catch {
            return null;
        }

        return null;
    }

    async function searchNearby(latitude, longitude) {
        if (!latitude || !longitude) {
            return null;
        }

        const params = new URLSearchParams({
            action: "query",
            format: "json",
            generator: "geosearch",
            ggscoord: `${latitude}|${longitude}`,
            ggslimit: "10",
            ggsnamespace: "6",
            ggsprimary: "all",
            ggsradius: "1000",
            iiprop: "url",
            iiurlwidth: "900",
            origin: "*",
            prop: "imageinfo"
        });

        try {
            const response = await fetch(`${commonsEndpoint}?${params}`);

            if (!response.ok) {
                return null;
            }

            const data = await response.json();

            if (!data.query || !data.query.pages) {
                return null;
            }

            const pages = Object.values(data.query.pages);

            for (const page of pages) {
                const info = page.imageinfo && page.imageinfo[0];

                if (info) {
                    const imageUrl = info.thumburl || info.url;

                    if (imageUrl) {
                        return imageUrl;
                    }
                }
            }
        } catch {
            return null;
        }

        return null;
    }

    async function loadImage(image) {
        const fullSearch = image.dataset.parkingImage || "";
        const latitude = image.dataset.latitude || "";
        const longitude = image.dataset.longitude || "";
        let commonsImage = null;

        if (fullSearch) {
            commonsImage = await searchCommons(fullSearch);
        }

        if (!commonsImage && fullSearch) {
            const locationName = fullSearch.split(",")[0];
            commonsImage = await searchCommons(locationName);
        }

        if (!commonsImage) {
            commonsImage = await searchNearby(latitude, longitude);
        }

        if (commonsImage) {
            image.src = commonsImage;
            return;
        }

        if (fallback) {
            image.src = fallback;
        }
    }

    images.forEach(function (image) {
        loadImage(image);
    });
});